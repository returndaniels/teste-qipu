#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

# 13/05/2021
# By: Daniel de Sousa da Silva
# gitlab.com/returndaniels/teste-qipu

from sys import version_info
from constants import enumerable_pt
from constants import mmbt_pt
from constants import exception_of_100_pt

def convert2Extensive(value):
    '''Converte valor inteiro para seu valor escrito por extenso em português

    Params:
    value (int): Valor que será escrito por extenso
    
    Returns:
    str: valor de entrada escrito por extenso
    '''
    _str = ""
    str_value = str(value)
    len_str_value = len(str_value)

    if(value < 20):
        _str = enumerable_pt[str(value)] + " "

    elif(value < 1000):
        key = str_value[0] + (len_str_value-1) * "0"
        str_len_key = str(len(key))
        modval = int(str_value[1:])

        _str += enumerable_pt[key] + " "

        if(key == "100" and modval !=0):
            _str = exception_of_100_pt + " "

        if(modval != 0):
            _str += "e " + convert2Extensive(modval)
    else:
        mmbt_pt_keys = mmbt_pt.keys()
        mod_by_3 = len_str_value%3
        miles = []
        _range = 0

        if(mod_by_3 > 0):
            miles.append(int(str_value[:mod_by_3]))

        for i in range(mod_by_3, len_str_value, 3):
            miles.append(int(str_value[i:i+3]))

        _range = len(miles)
        for i in range(_range):
            plural = 1
            miles_key = str(_range-i)
            
            if(miles[i]==1):
                plural = 0

            if miles_key in mmbt_pt_keys and miles[i]!=0:
                _str += convert2Extensive(miles[i]) + mmbt_pt[miles_key][plural]

    return _str


def convert2ExtensiveBRL(str_BRL):
    '''Converte valor em reais (BRL) para valor escrito por extenso em português

    Params:
    str_BRL (str): Valor em reais com centavos após a virgula e que será escrito por extenso
    
    Returns:
    str: valor de entrada escrito por extenso
    '''
    
    _values = str_BRL.split(",")
    _str = convert2Extensive(int(_values[0]))

    if(_values[0] == "1"):
        _str += "real "
    else:
        _str += "reais "

    if(len(_values) > 1 and int(_values[1]) != 0):
        _str += "e " + convert2Extensive(int(_values[1]))

        if(_values[1] == "01"):
            _str += "centavo "
        else:
            _str += "centavos "
        
    return _str

def read_lines(path="./input.txt"):
    '''Lê arquivo do caminho recebido como argumento

    Params:
    path (str): Caminho do arquivo que será lido
    
    Returns:
    List: Lista de linhas lidas pelo arquivo
    '''

    try:
        f = open(path)
        lines = f.readlines()
        f.close()
        return lines
    except:
        print("Erro na leitura do arquivo (" +path+ ")")
        return []

def write_lines(path, lines):
    try:
        f = open(path, "w")
        f.writelines(lines)
        f.close()
    except:
        print("Erro na leitura do arquivo (" +path+ ")")

def main():
    import os.path
    current_path = os.path.abspath(os.getcwd())

    input_filename = ""
    output_filename = ""

    if(version_info>(3, 0)):
        input_filename = input("Digite o caminho do arquivo de entrada: ")
        output_filename = input("Digite o caminho do arquivo de saida: ")
    else:
        input_filename = raw_input("Digite o caminho do arquivo de entrada: ")
        output_filename = raw_input("Digite o caminho do arquivo de saida: ")

    input_lines = read_lines(os.path.join(current_path, input_filename))
    output_lines = []

    for line in input_lines:
        line = line.strip()
        output_lines.append(line + " " + convert2ExtensiveBRL(line) + "\n")

    output_path = os.path.join(current_path, output_filename)
    if(os.path.exists(output_path)):
        output_path = os.path.join(current_path, output_filename + " (novo)")
    write_lines(output_path, output_lines)
    print("A saída do programa foi escrita em: " + output_path)

if __name__== "__main__":
   main()