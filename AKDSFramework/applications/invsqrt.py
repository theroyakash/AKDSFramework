import AKDSFramework.c.fsis
import rich

console = rich.console.Console()

def invsqrt(number: float):
    console.print(AKDSFramework.c.fsis.inverse_sqrt(number))