"""

Input: strs = ["flower","flow","flight"]
Output: "fl"

"""


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        prefixos = {}

        for string in strs:
            prefixo = string[:2]
            if prefixo in prefixos:
                prefixos[prefixo] += 1
            else:
                prefixos[prefixo] = 1

        prefixo_que_mais_repete = {}

        for chave, valor in prefixos.items():
            if len(prefixo_que_mais_repete) != 0:
                chave_maior, valor_maior = prefixo_que_mais_repete.popitem()

            if len(prefixo_que_mais_repete) == 0:
                prefixo_que_mais_repete = {chave: valor}
            elif valor > valor_maior:
                prefixo_que_mais_repete = {chave: valor}
            else:
                prefixo_que_mais_repete = {chave_maior: valor_maior}

        return prefixo_que_mais_repete


# strs = ["flower", "flow", "flight"]
strs = ["dog", "racecar", "car", "dog"]
prefixo = Solution()
prefixo_que_mais_repete = prefixo.longestCommonPrefix(strs)
print(prefixo_que_mais_repete)
