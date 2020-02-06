import json
import logging
import threading

from django.contrib.auth.decorators import permission_required
from django.core.files.storage import default_storage
from django.core.management import call_command
from django.http import Http404, HttpResponse

format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")


def list_gen_thread():
    logging.info("Starting list generation: Pack list")
    call_command("cs_generate_pack_list")
    logging.info("Starting list generation: Depot list")
    call_command("cs_generate_depot_list")
    logging.info("List generation done")


@permission_required("juntagrico.is_operations_group")
def generate_lists(request):
    thread = threading.Thread(target=list_gen_thread)
    thread.start()
    data = json.dumps({"list_generation": "started"})
    return HttpResponse(data, status=202, content_type="application/json")


@permission_required("juntagrico.is_operations_group")
def fetch_list_generation_date(request):
    filename = "depotlist.pdf"
    if default_storage.exists(filename):
        gen_date = default_storage.get_created_time(filename)
        gen_date = gen_date.strftime("%B %d, %Y %H:%M:%S %Z")
        data = json.dumps({"list_generation_date": gen_date})
        return HttpResponse(data, content_type="application/json")
    else:
        raise Http404(f"{filename} does not exist.")
