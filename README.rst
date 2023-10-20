Love is War
===========
Eliw (Engine Love is War) é uma engine para construção de jogos no estilo
clássico de **DOOM** com suporte frágil para dispositivos Android, sendo
uma engine ótima para construção de um verdadeiro passatempo para todos os
casais de plantão! Nessa engine, é possível ter todas as armas necessárias 
para a vitória nessa grande guerra do amor-*cof-cof*.

Para acessar a documentação do código e os textos de desenvolvimento,
por favor acesse o `pages do projeto`_. Como alternativa, é possível realizar
a compilação da documentação com o sphinx de maneira manual, processo explicado
em `Compilando a Documentação do Projeto`_.

.. _pages do projeto: https://lzunho-afk.github.io/love-is-war

Compilando a Documentação do Projeto
====================================
Para compilar a documentação e os respectivos comentários do código-fonte 
é possível utilizar o make (para usuários baseados em linux), o script
batch "make.bat" (para usuário de windows) ou o próprio sphinx (suporte
múltiplo).

* Para compilar com o make, utilize o comando ``make sphinx-docs``
* Com o script batch, execute-o da seguinte forma ``make.bat bdocs``
* Com o sphinx, utilizamos o **sphinx-apidoc** dentro do diretório *docs* e executamos o **sphinx-build**, da seguinte forma:

  .. code-block:: bash

    $ sphinx-apidoc -MPfe -o . .. ../setup.py ../loveiswar.py

  .. code-block:: bash

    $ sphinx-build . _build/

Materiais Externos
------------------
* Artworks
    * `p0ss`_: Algumas texturas utilizadas na fase de teste
    * `Iamrenz`_: Realistic Heart Sprite

.. _p0ss: https://opengameart.org/content/117-stone-wall-tilable-textures-in-8-themes
.. _Iamrenz: https://iamrenz.itch.io/real-heart
