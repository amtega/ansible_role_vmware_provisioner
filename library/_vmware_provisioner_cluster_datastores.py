#!/usr/bin/python
from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.vmware import PyVmomi, vmware_argument_spec


class VMwareHostFactManager(PyVmomi):
    def __init__(self, module):
        super(VMwareHostFactManager, self).__init__(module)
        hostnames = self.params.get('hosts')

        self.hosts = []
        for hostname in hostnames:
            hosts_found = self.get_all_host_objs(esxi_host_name=hostname)

            if len(hosts_found) > 1:
                self.module.fail_json(
                    msg="Hostname {h} matched multiple hosts".format(
                                                                h=hostname))
            if hosts_found is None:
                self.module.fail_json(
                    msg="Failed to find host system {h}.".format(h=hostname))

            self.hosts.append(hosts_found[0])

    def get_datastores(self):
        datastores = []
        datastores_names = []
        for host in self.hosts:
            for host_datastore in self.get_host_datastores(host):
                if host_datastore["name"] not in datastores_names:
                    datastores.append(host_datastore)
                    datastores_names.append(host_datastore["name"])
        self.module.exit_json(changed=False,
                              datastores=datastores)

    def get_host_datastores(self, host):
        datastores = []
        for datastore in host.datastore:
            datastore_info = {
                'name': datastore.summary.name,
                'total': datastore.summary.capacity,
                'free': datastore.summary.freeSpace,
            }
            datastores.append(datastore_info)
        return datastores


def main():
    argument_spec = vmware_argument_spec()
    argument_spec.update(
        hosts=dict(type='list', required=True),
    )
    module = AnsibleModule(argument_spec=argument_spec,
                           supports_check_mode=True)

    _vmware_provisioner_cluster_datastores = VMwareHostFactManager(module)
    _vmware_provisioner_cluster_datastores.get_datastores()


if __name__ == '__main__':
    main()
