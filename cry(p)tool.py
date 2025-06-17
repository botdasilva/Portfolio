# Importa bibliotecas necessárias
import sys                      # Para capturar argumentos da linha de comando
import hashlib                  # Para gerar hash (SHA-256) da senha
from cryptography.fernet import Fernet  # Para realizar criptografia simétrica (Fernet usa AES por baixo)
import base64                   # Para codificar o hash em base64 (formato compatível com Fernet)


# Função que gera uma chave a partir de uma senha
def generate_key(password):
    # Gera um hash SHA-256 da senha e converte para base64, que é o formato que o Fernet exige
    return base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest())


# Função para criptografar o arquivo
def encrypt(file_path, output, password):
    # Gera a chave baseada na senha fornecida
    key = generate_key(password)
    # Inicializa o objeto Fernet com essa chave
    f = Fernet(key)

    # Abre o arquivo de entrada no modo binário para leitura ('rb')
    with open(file_path, 'rb') as file:
        data = file.read()  # Lê todos os dados do arquivo

    # Criptografa os dados
    encrypted = f.encrypt(data)

    # Salva os dados criptografados no arquivo de saída no modo binário ('wb')
    with open(output, 'wb') as file:
        file.write(encrypted)

    # Mensagem de sucesso
    print(f"[+] File encrypted as {output}")


# Função para descriptografar o arquivo
def decrypt(file_path, output, password):
    # Gera a chave a partir da senha
    key = generate_key(password)
    # Inicializa o objeto Fernet com essa chave
    f = Fernet(key)

    # Abre o arquivo criptografado no modo binário para leitura
    with open(file_path, 'rb') as file:
        data = file.read()  # Lê os dados criptografados

    try:
        # Tenta descriptografar os dados
        decrypted = f.decrypt(data)
    except Exception:
        # Se a senha estiver errada ou o arquivo estiver corrompido
        print("[-] Invalid password or corrupted file!")
        return

    # Salva os dados descriptografados no arquivo de saída
    with open(output, 'wb') as file:
        file.write(decrypted)

    # Mensagem de sucesso
    print(f"[+] File decrypted as {output}")


# Bloco principal: executa quando roda o script via terminal
if __name__ == '__main__':
    # Verifica se foram passados exatamente 4 argumentos além do nome do script
    if len(sys.argv) != 5:
        print("Usage: python crypto_tool.py [encrypt/decrypt] [input_file] [output_file] [password]")
        sys.exit(1)  # Encerra o programa se os argumentos estiverem incorretos

    # Captura os argumentos da linha de comando
    command = sys.argv[1]       # encrypt ou decrypt
    input_file = sys.argv[2]    # arquivo de entrada
    output_file = sys.argv[3]   # arquivo de saída
    password = sys.argv[4]      # senha

    # Verifica qual operação realizar
    if command == 'encrypt':
        encrypt(input_file, output_file, password)
    elif command == 'decrypt':
        decrypt(input_file, output_file, password)
    else:
        print("Invalid command")  # Caso o comando não seja encrypt nem decrypt
