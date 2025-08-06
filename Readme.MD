# Salão de Beleza - Sistema de Agendamentos

## 📝 Sobre o Projeto

Sistema web desenvolvido com Django para gerenciamento de salões de beleza, focando em agendamentos, gestão de clientes e serviços. O projeto oferece uma interface intuitiva para recepcionistas e gerentes administrarem o dia a dia do estabelecimento.

## 🚀 Funcionalidades

- ✨ Gestão de Clientes
- 📅 Sistema de Agendamentos
- 💇‍♀️ Cadastro de Serviços
- 👥 Gestão de Profissionais
- 📊 Relatórios de Produtividade
- 🔐 Sistema de Permissões (Recepcionista/Gerente)

## 🛠 Tecnologias Utilizadas

- Python 3.9+
- Django 4.2+
- PostgreSQL
- Docker & Docker Compose
- Tailwind CSS
- HTMX

## 📋 Pré-requisitos

- Docker
- Docker Compose
- Git

## 🚀 Como executar o projeto

1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/salao-beleza.git
cd salao-beleza
```

2. Configure as variáveis de ambiente
```bash
cp .env.example .env
```

Exemplo de configuração do `.env`:
```properties
DEBUG=True
RABBITMQ_DEFAULT_USER=user
RABBITMQ_DEFAULT_PASS=password
```

4. Instale as dependências
```bash
pip install -r requirements.txt
```
e
4. Execute com Docker Compose
```bash
docker-compose up --build
```

5. Execute as migrações
```bash
python manage.py migrate
```

6. Crie um superusuário
```bash
python manage.py createsuperuser
```

## 👥 Tipos de Usuário

### Gerente
- Acesso total ao sistema
- Gestão de serviços
- Visualização de relatórios
- Gestão de profissionais

### Recepcionista
- Gestão de agendamentos
- Cadastro de clientes
- Visualização de agenda


## 📝 Comandos Úteis

```bash
# Iniciar os containers
docker-compose up

# Parar os containers
docker-compose down

```

## 📄 Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE.md](LICENSE.md) para detalhes.

## 🎯 Status do Projeto

Em desenvolvimento ativo. Novas funcionalidades sendo adicionadas regularmente.