"""patch para tornar CrewAI compatível com Windows"""
import signal
import platform

# adicionar sinais Unix faltantes no Windows
if platform.system() == 'Windows':
    # sinais que não existem no Windows
    sinais_unix = {
        'SIGHUP': 1,
        'SIGQUIT': 3,
        'SIGTRAP': 5,
        'SIGBUS': 7,
        'SIGKILL': 9,
        'SIGUSR1': 10,
        'SIGUSR2': 12,
        'SIGPIPE': 13,
        'SIGALRM': 14,
        'SIGCHLD': 17,
        'SIGCONT': 18,
        'SIGSTOP': 19,
        'SIGTSTP': 20,
        'SIGTTIN': 21,
        'SIGTTOU': 22,
        'SIGURG': 23,
        'SIGXCPU': 24,
        'SIGXFSZ': 25,
        'SIGVTALRM': 26,
        'SIGPROF': 27,
        'SIGWINCH': 28,
        'SIGIO': 29,
        'SIGPWR': 30,
        'SIGSYS': 31,
    }
    
    for nome, valor in sinais_unix.items():
        if not hasattr(signal, nome):
            setattr(signal, nome, valor)

import os
os.environ['CREWAI_TELEMETRY_DISABLE_SIGNALS'] = '1'