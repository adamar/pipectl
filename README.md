
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
  - 'retries' (Optional)

- bashRunCommand
  - 'id' (Optional)
  - 'cmd' (Required) 
  - 'retries' (Optional)

- notifyViaSlack
  - 'id' (Optional)
  - 'channel' (Required)
  - 'message' (Required)
  - 'tag' (Optional)
  - 'retries' (Optional)



