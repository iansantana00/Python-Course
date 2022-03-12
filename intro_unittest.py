"""
Introdução ao módulo Unittest

Unittest -> Testes Unitários

O que são testes unitários?

Teste é a forma de se testar unidades individuais de código fonte.

Unidade individuais podem ser: Funções, métodos, classes, módulos etc.

# OBS: Teste unitário não é específico da linguagem Python.

Para criar nossos teste, criamos classes que herdam de unittest.Testcase
e a partir de então ganhamos todos os 'assertions' presentes no módulo,

Para rodar os testes, utilizamos unittest.main()

TestCase -> Casos de teste para sua unidade

# Conhecendo as assertions
https://docs.python.org/3/library/unittest.html

Método                      Checa se
assertEqual(a, b)           a == b
assertNotEqual(a, b)        a != b
assertTrue(x)               x é verdadeiro
assertFalse(x)              x é falso
assertIs(a, b)              a é b
assertIsNot(a, b)           a não é b
assertIsNotNone(x)          x é None
assertNotIn(a, b)           a está em b
assertIsInstance(a, b)      a não está em b
assertIsInstance(a, b)      a é instância de b
assertNotIsInstance(a, b)   a não é instânica de b

Por convenção, todos os testes em um test case, devem ter o nome
iniciado com test_


"""
