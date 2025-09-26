## Testes BDD com BehaveX + Behave
### Requisitos

Python 3.x instalado

Git (opcional, se for clonar um repositório)

BehaveX é um wrapper do Behave, com execução paralela e relatórios. Instala-se via: pip install behavex e executa pelo comando: behavex.

## Criar e ativar o ambiente virtual

### Windows (PowerShell)
python -m venv .venv

.\\.venv\Scripts\Activate.ps1

python -m pip install   --upgrade pip

### macOS / Linux
python3 -m venv .venv

source .venv/bin/activate

python -m pip install --upgrade pip

## Instalar dependências
pip install -r requirements.txt

## Para rodar o projeto
behavex -t @tag
## Caso queria rodar todos os testes
behavex
## Estrutura do projeto

├─ features/   
   ├─ data # Para futuro json   
│  ├─ planets.feature   
│  ├─ species.feature   
│  ├─ steps/   
│  │  ├─ planets_step.py   
│  │  └─ species_steps.py   
│  └─ environment.py   
├─ utils/   
│  └─ service.py   
├─ requirements.txt   
└─ README.md   

## Caso queira abrir o relátorio:
Após rodar os testes, abra a pasta output, clique com o botão direto em report.html, clique em abrir com e escolha o navegador de preferência. 
