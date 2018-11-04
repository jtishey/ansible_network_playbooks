---
- hosts: "{{ my_hosts }}"
  gather_facts: no
  connection: local

  tasks:
  - name: Backup Juniper running configuration
    junos_config:
      backup: yes
