---
- hosts: vSRX1
  gather_facts: no
  connection: local

  tasks:
  - name: Setting ISIS overload
    junos_config:
      lines: 
        - delete protocols isis overload timeout
        - set protocols isis overload advertise-high-metrics
    register: result

  - name: print result
    debug: var=result
