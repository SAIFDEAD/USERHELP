# 𝐹𝜃𝜄𝜄𝜃𝜛 𝜏𝜆𝑖𝑠 𝑓𝜃𝛾𝑚𝛼𝜏 𝜏𝜃 𝑚𝛼𝜅𝜀 𝜓𝜃𝜇𝛾 𝜃𝜛𝜂 𝜌𝜄𝜇𝑔𝑖𝜂 𝑓𝜃𝛾 𝑆𝛼𝑖𝑓 𝑈𝑠𝜀𝛾 𝛣𝜃𝜏𝑠.

```python3
"""
A sample code to display hello without taking input.
"""
# this is a mandatory import
from . import *

# assigning command
@hell_cmd(pattern="hii$")
async def hi(event):
    # command body
    await eor(event, "Hello!")


# to display in help menu
CmdHelp("hii").add_command(
  "hii", None, "Says Hello!"
).add()
```

```python3
"""
A sample code to display hello with input.
"""
# this is a mandatory import
from . import *

# assigning command
@hell_cmd(pattern="hii(?:\s|$)([\s\S]*)")
async def hi(event):
    # command body
    _input = event.pattern_match.group(1)
    if _input:
        await eor(event, f"Hello! {_input}")
    else:
        await eor(event, "Hello!")


# to display in help menu
CmdHelp("hii").add_command(
    "hii", "<text>", "Display Hello with a input!"
).add()
```


## To get more functions read codes in repo.
