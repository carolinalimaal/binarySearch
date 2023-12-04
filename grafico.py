import matplotlib.pyplot as mplt

x = [
    10,
    50,
    100,
    500,
    1000,
    5000,
    10000,
    50000,
    100000,
    500000,
    1000000,
    5000000,
    10000000,
    50000000

]

y = [
    0.0027291000001241628,
    0.003913300000021991,
    0.00444389999984196,
    0.005939499999840336,
    0.006530800000291492,
    0.008842500000355358,
    0.009736900000461901,
    0.011082699999860779,
    0.012499500000558328,
    0.01357099999950151,
    0.014019100000041362,
    0.016123599999446014,
    0.01700260000052367,
    0.01865379999981087
]   

mplt.plot(x, y, color= 'orange')
mplt.title('Tempo de execução x Tamanho do vetor')
mplt.xlabel('Tamanho do vetor')
mplt.ylabel('Tempo de execução (s)')
mplt.legend('Blue line = IterativeBinarySearch')
mplt.show()
