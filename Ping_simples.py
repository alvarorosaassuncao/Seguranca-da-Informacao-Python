import os ## Importando o modulo ou biblioteca OS (integra os programas e recursos do sistema operacional.

print('#' * 60) ## Imprimindo # 60 vezes
ip_ou_host = (input("Digite o IP ou HOST a ser verificado:")) # Criamos uma variavel que irá receber um usuário e um  IP

print('-' * 60) ## Imprimindo - 60 vezes

os.system('ping -n 6 {}'.format(ip_ou_host)) ##Chamando system da biblioteca OS - comando ping -n -num de pacotes  que serão 6{}

print('-' * 60)
