
def classificar_mensagem(mensagem):
    texto = mensagem.lower()

    if "preço" in texto or "orçamento" in texto:
        return "Comercial"

    elif "erro" in texto or "problema" in texto:
        return "Suporte Técnico"

    elif "currículo" in texto or "vaga" in texto:
        return "Recursos Humanos"

    else:
        return "Análise Manual"


print("========================")
print("ASSISTENTE DE ATENDIMENTO")
print("========================")

mensagem = input("Digite a mensagem do cliente: ")

categoria = classificar_mensagem(mensagem)

print("\nResultado da análise:")
print("Mensagem:", mensagem)
print("Categoria:", categoria)
