#!/usr/bin/python
from __future__ import absolute_import, division, print_function
__metaclass__ = type


from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.vmware import (find_cluster_by_name,
                                         find_datacenter_by_name,
                                         vmware_argument_spec,
                                         PyVmomi)


class VmwareConfigInfoManager(PyVmomi):
    def __init__(self, module):
        super(VmwareConfigInfoManager, self).__init__(module)
        datacenter_name = self.params.get('datacenter_name')
        cluster_name = self.params.get('cluster_name')
        self.hosts = self.get_all_hosts_by_datacenter_cluster(
                                            datacenter_name=datacenter_name,
                                            cluster_name=cluster_name)

    def get_all_hosts_by_datacenter_cluster(self,
                                            datacenter_name,
                                            cluster_name):
        """Get all hosts from cluster by datacenter and cluster name"""
        datacenter_obj = find_datacenter_by_name(
                                            self.content,
                                            datacenter_name=datacenter_name)
        cluster_obj = find_cluster_by_name(self.content,
                                           cluster_name=cluster_name,
                                           datacenter=datacenter_obj)
        if cluster_obj:
            return [host for host in cluster_obj.host]
        else:
            return []

    def gather_hosts(self):
        cluster_hosts = []
        for host in self.hosts:
            cluster_hosts.append(host.name)
        return cluster_hosts


def main():
    argument_spec = vmware_argument_spec()
    argument_spec.update(
        datacenter_name=dict(type='str', required=True),
        cluster_name=dict(type='str', required=True),
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True
    )

    vmware_provisioner_cluster_hosts = VmwareConfigInfoManager(module)
    module.exit_json(
        changed=False,
        hosts=vmware_provisioner_cluster_hosts.gather_hosts())


if __name__ == "__main__":
    main()
