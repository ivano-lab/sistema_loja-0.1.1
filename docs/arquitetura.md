## Estrutura do Projeto


    sistema_loja-0.1.1/
    │── main.py                  # Ponto de entrada do sistema
    │── loja.db                  # Banco SQLite (recomenda-se mover para /data) 
    │── requirements.txt         # Dependências do projeto (se houver) 
    │ 
    ├── data/                    # Banco e scripts de migração 
    │   ├── loja.db 
    │   └── migrations/          # Scripts para alteração do schema (ex: migrate_vendas.py) 
    │ 
    ├── utils/                   # Regras de negócio e lógica funcionando no terminal 
    │   ├── __init__.py 
    │   ├── db.py                # Conexão com o banco 
    │   ├── produto.py           # CRUD de produtos 
    │   ├── cliente.py           # CRUD de clientes
    │   ├── venda.py             # Módulo de vendas
    │   ├── relatorio.py         # Geração de relatórios
    │   └── utils.py             # Funções auxiliares (ex: formatar moeda)
    │
    ├── gui/                     # Telas do sistema feitas em Tkinter
    │   ├── __init__.py
    │   ├── tela_inicial.py
    │   ├── tela_produtos.py
    │   ├── tela_clientes.py
    │   ├── tela_vendas.py
    │   └── componentes/         # Elementos visuais reutilizáveis (botões, navegadores etc.)
    │
    ├── ui/                      # Protótipos e testes de interface
    │   ├── mockups/             # Wireframes e ideias visuais
    │   └── testes/              # Experimentações com Tkinter e ttk
    │
    └── tests/                   # Testes unitários
        ├── __init__.py
        ├── test_produto.py
        ├── test_cliente.py
        └── test_venda.py

