# features/environment.py
import os
import logging
from datetime import datetime
from utils.service import ApiClient

def before_all(context):
    context.base_url = os.getenv("BASE_URL", "https://swapi.dev/api/")
    context.client = ApiClient(context.base_url)

    context.output_dir = os.path.join(os.getcwd(), "output")
    os.makedirs(context.output_dir, exist_ok=True)


    log_file = os.path.join(context.output_dir, "logs", f"behave_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    context.logger = logging.getLogger("behave")

    context.logger.info("===== Início da execução dos testes =====")

def before_feature(context, feature):
    context.logger.info(f"Iniciando feature: {feature.name}")

def before_scenario(context, scenario):
    context.logger.info(f"--> Cenário: {scenario.name}")

def after_scenario(context, scenario):
    status = "PASSOU" if scenario.status == "passed" else f"FALHOU ({scenario.status})"
    context.logger.info(f"<-- Cenário finalizado: {scenario.name} -> {status}")

def after_feature(context, feature):
    context.logger.info(f"Feature finalizada: {feature.name}")

def after_all(context):
    context.logger.info("===== Fim da execução dos testes =====")
