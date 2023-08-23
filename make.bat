@ECHO OFF

rem Dev. Commandline - Loveiswar Engine (LIWE) 
type LICENSE
echo:

rem Ajustando o virtualenv do python conforme necessário
if EXIST .venv\Scripts\activate.bat (
    .venv\Scripts\activate.bat
) else (
    CALL :setupenv
)

rem Variáveis de uso global
set DOCS_PATH=".\docs"
set DOCS_BATCH="%DOCS_PATH%\make.bat"

rem Realizando o parsing dos argumentos da linha de comando
IF "%1" == "" GOTO help
IF "%1" == "documentation" GOTO bdocs
IF "%1" == "setupenv" GOTO setupenv
IF "%1" == "clean" GOTO clean
EXIT /B %ERRORLEVEL%

:bdocs
rem Compilação da documentação com Sphinx
pushd .\docs
sphinx-apidoc -o . .. ..\setup.py
make.bat html
popd
GOTO end

:clean
IF "%2" == "" GOTO cleanall
IF "%2" == "documentation" GOTO cleandocs
IF "%2" == "venv" GOTO cleanvenv
echo "=> Opcao de limpeza invalida! - '%2'"
GOTO help

:cleanall
rem Chama todas as funções de limpeza
CALL cleandocs
CALL cleanvenv
EXIT /B 0

:cleandocs
rem Remove os arquivos gerados para documentação
echo Removendo os arquivos de documentacao do projeto, para recupera-los chame a operacao 'documentation'.
rmdir .\docs\_build /s /q
del .\docs\modules.rst
del .\docs\loveiswar.rst
EXIT /B 0

:cleanvenv
rem Remove o python venv do projeto
echo Removendo o venv do projeto, para recupera-lo chame o 'setupenv' ou rode o programa normalmente.
rmdir .\.venv /s /q
EXIT /B 0

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
echo                            \- * documentation; * venv; * package.
echo                            \- ex.: .\make.bat clean documentation
echo:

:end
