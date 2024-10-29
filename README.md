# fastfood-lambda-auth

Essa função Lambda gerencia a autenticação para um pool de usuários do Cognito. Ela recebe um pedido com o CPF do usuário e tenta registrá-lo através do método `sign_up` do Cognito. Se o registro for bem-sucedido, a função inicia o processo de autenticação e retorna uma resposta correspondente.

## Informacoes de como consumir

A função aguarda uma solicitação HTTP com um payload JSON que inclui o CPF do usuário:

### Corpo da solicitação
```json
{
  "body": "{\"cpf\":\"CPF_DO_USER\"}"
}
```

### Resposta
A função devolve um objeto JSON estruturado da seguinte forma:

- `statusCode`: Código de status HTTP da resposta.
- `body`: Objeto JSON com uma mensagem e a resposta de autenticação.

Exemplo de resposta não autorizada:

```json
{
  "statusCode": 401,
  "body": "{\"message\":\"User nao autorizado\"}"
}
```

Exemplo de resposta de erro generico:

```json
{
"statusCode": 500,
"body": "{\"message\":\"Erro generico: ...\"}"
}
```

Exemplo de resposta bem-sucedida:

```json
{
  "statusCode": 200,
  "body": "{\"message\":\"User autenticado com sucesso\",\"response\":{\"AuthenticationResult\":{...}}}"
}
```

