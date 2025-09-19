from playwright.sync_api import Page, expect

def test_pagina_inicial_carrega(page: Page):
    """
    Teste simples para verificar se a página inicial de um e-commerce carrega.
    """
    # Navega até um e-commerce de sua escolha
    page.goto("https://www.magazineluiza.com.br/")

    # Verifica se o título da página contém o nome da loja
    expect(page).to_have_title("Magazine Luiza | Pra você é Magalu!")