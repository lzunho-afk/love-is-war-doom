@ECHO OFF

rem Dev. Commandline - Loveiswar Engine (LIWE)
type LICENSE
echo:

rem Ajustando o virtualenv do python conforme necessário
if EXIST .venv\Scripts\activate.bat (
    .venv\Scripts\activate.bat
) else (
    CALL setupenv
)

rem Variáveis de uso global
set DOCS_PATH=".\docs"
set DOCS_BATCH="%DOCS_PATH%\make.bat"

rem Realizando o parsing dos argumentos da linha de comando
IF "%1" == "" GOTO help
IF "%1" == "documentation" GOTO bdocs

:bdocs
rem Compilação da documentação com Sphinx
pushd .\docs
sphinx-apidoc -o . .. ..\setup.py
make.bat html
popd
GOTO end

:setupenv
rem Configuração do venv para o ambiente
python -m pip install -U venv
python -m venv .venv
.venv\Scripts\activate.bat
python -m pip install -U pip
python -m pip install -r requirements.txt
EXIT /B 0

:help
echo PAINEL DE AJUDA:
echo    * documentation     - Compila a documentacao com sphinx.
echo    * setupenv          - Roda os comandos de definição do venv da engine.
echo    * package           - Realiza o empacotamento do projeto (nao funciona).
echo    * clean             - Realiza a limpeza de todas as operacoes caso nenhuma
echo                           seja especificada individualmente.
echo                            \- * documentation; * requirements; * package.
echo                            \- ex.: .\make.bat clean documentation
echo:

:end