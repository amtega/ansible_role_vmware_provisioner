# Ansible vmware_provisioner role

This is an [Ansible](http://www.ansible.com) role to setup VMware virtual machines.

## Requirements

[Ansible 2.7+](http://docs.ansible.com/ansible/latest/intro_installation.html)

## Role Variables

A list of all the default variables for this role is available in `defaults/main.yml`. The role setups the following facts:

- vmware_provisioner_vms_basic_facts: gathered virtual machines basic facts
- vmware_provisioner_vms_detailed_facts: gathered virtual machines detailed facts
- vmware_provisioner_inventory_vms: virtual machines configs foind in the inventory

## Dependencies

- [amtega.check_platform](https://galaxy.ansible.com/amtega/check_platform)
- [amtega.packages](https://galaxy.ansible.com/amtega/packages)
- [amtega.select_hostvars](https://galaxy.ansible.com/amtega/select_hostvars)

## Example Playbook

This is an example playbook:

```yaml
---

- hosts: all
  roles:
    - role: amtega.vmware_provisioner
      vmware_provisioner_hostname: vcenter.acme.com
      vmware_provisioner_username: username
      vmware_provisioner_password: password
      vmware_provisioner_validate_certs: no
      vmware_provisioner_testing_vms:
        - name: "my_vm"
          annotation: Ansible provisioned vm
          folder: /
          guest_id: centos7_64Guest
          hardware:
            memory_mb: 512
            num_cpus: 1
            num_cpu_cores_per_socket: 1
          datacenter: dc
          cluster: cluster
          disk:
            - size_gb: 30
              type: thin
              datastore: datastore            
          wait_for_ip_address: no          
          force: yes
```

## Testing

To run test you must point the variable `vmware_provisioner_tests_host` to a host that can be managed with ansible and that has access to an existing vCenter/ESXi.

Also yo must provide the following minimim role variables (see `defaults/main.file` for details):

- `vmware_provisioner_hostname`
- `vmware_provisioner_username`
- `vmware_provisioner_password`
- `vmware_provisioner_vm_datacenter`
- `vmware_provisioner_vm_cluster`
- `vmware_provisioner_vm_disk`

One way to provide this information is calling the testing playbook passing the host to use and an additional vault inventory plus the default one provided for testing, as it's show in this example:

```shell
$ cd amtega.vmware_provisioner/tests
$ ansible-playbook main.yml -e "vmware_provisioner_tests_host=test_host" -i inventory -i ~/mycustominventory.yml --vault-id myvault@prompt
```

## License

Copyright (C) 2018 AMTEGA - Xunta de Galicia

This role is free software: you can redistribute it and/or modify it under the terms of:

GNU General Public License version 3, or (at your option) any later version; or the European Union Public License, either Version 1.2 or – as soon they will be approved by the European Commission ­subsequent versions of the EUPL.

This role is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details or European Union Public License for more details.

## Author Information

- Juan Antonio Valiño García.
- This role is based on [geerlingguy.vmware_provisioner](https://galaxy.ansible.com/geerlingguy/vmware_provisioner) role.
