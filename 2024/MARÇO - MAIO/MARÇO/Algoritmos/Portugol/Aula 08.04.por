programa {
    funcao inicio() {
        // Declaração de variáveis
        inteiro quantidadeDocumentosApresentados, vagasDisponiveis
        cadeia resposta
        
        // Inicialização das variáveis
        quantidadeDocumentosApresentados = 0
        vagasDisponiveis = 30
        
        // Solicitação de matrícula
        escreva("Bem-vindo à Escola Municipal. Por favor, solicite a matrícula do aluno.\n")
        
        // Fornecimento de documentos
        escreva("\nPor favor, apresente os seguintes documentos:\n")
        escreva("- Certidão de Nascimento\n")
        escreva("- Comprovante de Residência\n")
        escreva("- Histórico Escolar\n")
        
        // Verificação de documentos
        escreva("\nO aluno apresentou a Certidão de Nascimento? (s/n): ")
        leia(resposta)
        se (resposta == "s") {
            quantidadeDocumentosApresentados = quantidadeDocumentosApresentados + 1
        }
        
        escreva("O aluno apresentou o Comprovante de Residência? (s/n): ")
        leia(resposta)
        se (resposta == "s") {
            quantidadeDocumentosApresentados = quantidadeDocumentosApresentados + 1
        }
        
        escreva("O aluno apresentou o Histórico Escolar? (s/n): ")
        leia(resposta)
        se (resposta == "s") {
            quantidadeDocumentosApresentados = quantidadeDocumentosApresentados + 1
        }
        
        // Verificação de vagas disponíveis
        se (quantidadeDocumentosApresentados == 3 e vagasDisponiveis > 0) {
            // Efetivação da matrícula
            escreva("\nMatrícula efetivada com sucesso!\n")
            escreva("Bem-vindo à nossa escola!\n")
            vagasDisponiveis = vagasDisponiveis - 1
        } senao {
            se (quantidadeDocumentosApresentados != 3) {
                escreva("\nA matrícula não pode ser efetivada. Todos os documentos necessários devem ser apresentados.\n")
            } senao {
                escreva("\nNão há vagas disponíveis para a turma desejada. Matrícula não realizada.\n")
            }
        }
    }
}








/*
programa {
    // Função principal do programa
    funcao inicio() {
        // Quantidade total de processos
        inteiro totalProcessos = 0
        
        // Solicitar ao usuário o período desejado (mês a mês)
        inteiro mes
        enquanto (verdadeiro) {
            escreva("\nInforme o mês desejado (1 a 12, 0 para sair): ")
            leia(mes)
            
            // Verificação do mês e exibição da quantidade de processos
            se (mes >= 1 e mes <= 12) {
                // Consulta a quantidade de processos do mês
                inteiro processoMes

                se (mes == 1) {
                    processoMes = 100
                } senao {
                    se (mes == 2) {
                        processoMes = 110
                    } senao {
                        se (mes == 3) {
                            processoMes = 120
                        } senao {
                            se (mes == 4) {
                                 processoMes = 130
                            } senao {
                                se (mes == 5) {
                                     processoMes = 140
                                } senao {
                                    se (mes == 6) {
                                         processoMes = 150
                                    } senao {
                                        se (mes == 7) {
                                             processoMes = 160
                                        } senao {
                                            se (mes == 8) {
                                                 processoMes = 170
                                            } senao {
                                                se (mes == 9) {
                                                    processoMes = 180
                                                } senao {
                                                    se (mes == 10) {
                                                         processoMes = 190
                                                    } senao {
                                                        se (mes == 11) {
                                                             processoMes = 200
                                                        } senao {
                                                            se (mes == 12) {
                                                                 processoMes = 210
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
                
                // Exibir quantidade de processos no mês específico
                escreva("Quantidade de processos no mês ", mes, ": ",  processoMes, "\n")
                
                // Adiciona a quantidade de processos do mês ao total
                totalProcessos = totalProcessos +  processoMes
            } senao {
                se (mes == 0) {
                    // Se o usuário digitou 0, exibe o total de processos e encerra o programa
                    escreva("Total de processos em todos os meses: ", totalProcessos, "\n")
                    pare
                } senao {
                    escreva("\nMês inválido. O mês deve estar entre 1 e 12.\n")
                }
            }
        }
    }
}




*/ 



/* 
programa {
    funcao inicio() {

        inteiro opcao, saldo, precoSabonete, precoMacarrao, precoPapel, produtoSelecionado

        // Inicializa o saldo e os preços dos produtos
        saldo = 1000
        precoSabonete = 30
        precoMacarrao = 300
        precoPapel = 0

        //inicio

        enquanto (verdadeiro) {
            escreva("\nSelecione uma Opção:\n")
            
            escreva("1. Consultar produto\n")
            escreva("2. Realizar compra\n")
            escreva("3. Falar com Atendente\n")
            escreva("4. Consultar saldo\n")
            escreva("5. Sair\n")

            escreva("Opção: ")
            leia(opcao)

            // base

            se (opcao == 1) {
                escreva("\n---------------------\n")
                escreva("Produtos: \n")
                escreva("1. Sabonete: ", precoSabonete, " conto\n")
                escreva("2. Macarrão: ", precoMacarrao, " conto\n")
                escreva("3. Papel: ", precoPapel, " conto\n")
                escreva("---------------------\n")
            }

            se (opcao == 2) {
                escreva("\n--------------------------------------\n")
                escreva("O que gostaria de comprar?(Digite o número correspondente): ")
                leia(produtoSelecionado)

                // Verifica o produto selecionado e o saldo disponível
                se (produtoSelecionado == 1 e saldo >= precoSabonete) {
                    saldo = saldo - precoSabonete
                    escreva("\nVocê comprou um Sabonete por ", precoSabonete, " conto.\n")
                    escreva("Saldo restante: ", saldo, " conto\n")
                } senao {
                    se (produtoSelecionado == 2 e saldo >= precoMacarrao) {
                        saldo = saldo - precoMacarrao
                        escreva("\nVocê comprou um Macarrão por ", precoMacarrao, " conto.\n")
                        escreva("Saldo restante: ", saldo, " conto\n")
                    } senao {
                        se (produtoSelecionado == 3 e saldo >= precoPapel) {
                            saldo = saldo - precoPapel
                            escreva("\nVocê comprou uma Papel por ", precoPapel, " conto.\n")
                            escreva("Saldo restante: ", saldo, " conto\n")
                        } senao {
                            escreva("\nSaldo insuficiente ou opção inválida. Tente novamente.\n")
                        }
                    }
                }
            }

            se (opcao == 3) {
                escreva("\nFavor aguardar, você será conectado com um de nossos atendentes.\n")
            }

            se (opcao == 4) {
                escreva("\n---------------------\n")
                escreva("Saldo restante: ", saldo, " conto\n")
                escreva("---------------------\n")
            }            

            se (opcao == 5) {
                escreva("Programa encerrado.\n")
                pare
            }

        }
    }
}

*/









