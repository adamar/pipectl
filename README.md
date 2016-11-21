
# PipeCTL

Define a Pipeline for builds in YAML


## Example:

```
---
- bambooBuildAndWait:
    id: 
    jobs: []

- bashRunCommand:
    id: 
    cmd: 'ping -c 1 google.com'

```

## Methods 

- bambooBuildAndWait
  - 'id' (Optional)
  - 'jobs' (Required)

- bashRunCommand
  - 'id' (Optional)
  - 'cmd' (Required) 

- notifyViaSlack
  - 'id' (Optional)
  - 'channel' (Required)
  - 'message' (Required)
  - 'tag' (Optional)



