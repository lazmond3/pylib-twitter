"Debug" Module Repository
========================

DEBUG=1 python3 ....

^ can be detected with "os.getenv("DEBUG")" and export "DEBUG"

```
if DEBUG:
    print("hello world ! this is debug mode...")
```