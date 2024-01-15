HEY! Parece que você acabou de encontrar meu reposítorio com testes de injeção para o BancoCN.

* Como rodo?

+ Primeiro copie o arquivo conf.example.json para conf.json e mude conforme o necessário.
+ instale as dependencias do requirements.txt
+ rode o payload.py ou o autoshell.py

* Servindo um index.php diferente:
++ é só rodar o seguinte comando:
$ cat payload-test/index.php | nc -lnvp <SUA PORTA>

* Como eu escuto o reverse shell? 
++ Simples! Rode o comando abaixo:
$ nc -lnvp <SUA PORTA>

* CREDITOS
 = RyDiffusion pelo código
 = openbsd60 pela ideia
 = Pentest monkey pelo Reverse Shell: https://github.com/pentestmonkey/php-reverse-shell