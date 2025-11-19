# Processador Simples de Texto

Este repositório contém um script Python simples que lê um arquivo `entrada.txt`, aplica regras de transformação ao seu conteúdo e grava o resultado em `saida.txt`, garantindo que o arquivo original permaneça inalterado.

## O que o programa faz
- Lê `entrada.txt` (arquivo de texto no mesmo diretório).
- Remove qualquer linha que contenha a substring "ignor" (case-insensitive), o que abrange palavras como "ignorar", "ignorada", etc.
- Substitui todas as ocorrências da palavra "problema" por "desafio", preservando plural e capitalização (por exemplo: "Problemas" → "Desafios").
- Mantém todas as demais linhas intactas.
- Grava o conteúdo processado em `saida.txt`. O arquivo `entrada.txt` NÃO é modificado.

## Requisitos
- Python 3.8+ instalado.
- Nenhuma biblioteca externa necessária (usa apenas a stdlib).

## Arquivos neste diretório
- `process_text.py` — script Python que realiza o processamento.
- `entrada.txt` — exemplo de arquivo de entrada (você pode criar/editar).
- `saida.txt` — arquivo de saída gerado pelo script (será criado/atualizado ao executar).

## Conteúdo de exemplo para `entrada.txt`
Você pode criar um arquivo `entrada.txt` com este conteúdo de exemplo:

Este é um problema simples.
Podemos resolver este problema facilmente.
Esta linha deve ser ignorada.
Outro problema aparece aqui.
Linha comum sem problemas.

## Como executar
1. Abra um terminal/console.
2. Navegue até a pasta onde estão `process_text.py` e `entrada.txt`.
3. Execute:
```bash
python process_text.py
```
4. Após a execução, verifique o arquivo `saida.txt` gerado no mesmo diretório.

## Resultado esperado (exemplo)
A partir do exemplo acima, `saida.txt` deverá conter:

Este é um desafio simples.
Podemos resolver este desafio facilmente.
Outro desafio aparece aqui.
Linha comum sem desafios.

Observação: a linha contendo "ignorar" foi removida e todas as ocorrências de "problema" foram substituídas por "desafio".

## Detalhes de implementação
- A substituição de "problema" usa expressão regular e um callback para:
  - Preservar plural (adiciona "s" quando presente).
  - Preservar capitalização da primeira letra (ex.: "Problema" → "Desafio"; "PROBLEMA" → "DESAFIO").
- A remoção de linhas é feita buscando a substring "ignor" sem diferenciar maiúsculas/minúsculas. Se preferir remover apenas linhas com a palavra exata "ignorar", a regex pode ser ajustada.
- O script lê o arquivo preservando quebras de linha originais e grava o resultado em `saida.txt`, portanto `entrada.txt` permanece intacto.
- Codificação: o script usa UTF-8 ao ler/escrever arquivos.

## Observações e recomendações
- Se for trabalhar com arquivos muito grandes, considere adaptar o script para processar linha-a-linha em streaming, reduzindo uso de memória.
- Se precisar de correspondência somente para a palavra completa "ignorar" (e não substrings), a regex pode ser trocada por algo como `\bignorar\b`, com flags apropriadas.
- Teste com variações de maiúsculas/minúsculas, plural e acentuação para verificar o comportamento desejado.

## Como testar automaticamente (opcional)
Você pode criar um pequeno teste manual:
1. Faça uma cópia de `entrada.txt` (por segurança).
2. Execute o script.
3. Compare `saida.txt` com o resultado esperado (visualmente ou usando `diff` no terminal):
```bash
diff entrada.txt saida.txt
```
Note que `diff` mostrará diferenças; como objetivo é que `saida.txt` seja diferente (processado), use `diff` com um arquivo de referência esperado para validar.

## Possíveis melhorias
- Adicionar opção de linha de comando para personalizar nomes de arquivos (ex.: `--in`, `--out`).
- Permitir escolher entre remover linhas que contenham substrings ou apenas palavras inteiras.
- Adicionar testes automatizados (pytest) cobrindo casos com maiúsculas, plural e linhas com "ignorar".
- Suportar processamento recursivo de diretórios ou múltiplos arquivos.

## Licença
Sinta-se livre para usar e adaptar este código conforme necessário. Se for para um projeto público, recomendo adicionar uma licença (ex.: MIT) ao repositório.
