# Pulumi configs are set via the terminal or in the step process in Octopus Deploy
# pulumi config set --secret clientSecret your_secret
# pulumi config set clientID your_client_id

import logging
import pulumi
import aksParamConstants as constants
from pulumi_azure import containerservice, core
    

def createAKSCluster():
    config = pulumi.Config()

    if containerservice == None:
        logging.warning("Check to ensure the containerservice import is accurate")
    
    else:
        containerservice.KubernetesCluster(
            resource_name = constants.name,
            default_node_pool={
                'min_count': constants.min_count,
                'max_count': constants.max_count,
                'name': constants.name,
                'vm_size': constants.vm_size,
                'enable_auto_scaling': constants.auto_scaling
            },
            dns_prefix=constants.dns_prefix,    
            resource_group_name=constants.resource_group_name,
            service_principal={
                'client_id': constants.clientID,
                'client_secret': config.require_secret('clientSecret')
                }
            )

createAKSCluster()