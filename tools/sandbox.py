import sys
import io
import contextlib
import traceback
import asyncio

def _execute_python_sync(code: str):
    """
    Executes Python code and captures the output.
    """
    output_buffer = io.StringIO()
    
    # Execution context (globals/locals). 
    # We use a fresh dict to avoid clashing with the server's variables.
    exec_globals = {"__builtins__": __builtins__}
    
    try:
        with contextlib.redirect_stdout(output_buffer), contextlib.redirect_stderr(output_buffer):
            exec(code, exec_globals)
            
        return output_buffer.getvalue() or "[Code executed successfully with no output]"
        
    except Exception:
        # If an error occurs, return the output so far + the traceback
        return output_buffer.getvalue() + "\n" + traceback.format_exc()

async def execute_python(code: str) -> str:
    """
    Execute arbitrary Python code and return the output (stdout and stderr).
    Useful for precision math, data processing, or logic tasks.
    
    Args:
        code (str): The valid Python code to execute.
    """
    return await asyncio.to_thread(_execute_python_sync, code)
