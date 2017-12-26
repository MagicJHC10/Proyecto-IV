Vagrant.configure('2') do |config|
  config.vm.box = 'azure'
  config.vm.box_url = 'https://github.com/msopentech/vagrant-azure/raw/master/dummy.box' #Caja base vacía
  # use local ssh key to connect to remote vagrant box
  config.ssh.private_key_path = '~/.ssh/id_rsa'
  config.vm.network "public_network" 
  config.vm.network "forwarded_port", guest: 80, host: 80

  config.vm.provider :azure do |azure, override|


    # configuration needed for Azure
    azure.tenant_id = '8c330b7f-76ef-449c-983b-294ff925b9cd'
    azure.client_id = 'ebab5eb4-c3d5-46e0-893b-34638ef78cbb'
    azure.client_secret = 'upWEVHF8wq1Nor32HtuJ96G3BB+hOmWVA/9/BeDTaC0='
    azure.subscription_id = '37160be2-7b11-4655-bdfe-44715bbb400a'
    azure.vm_size = "Standard_DS2_v2"
  end

  # configuration of ansible
  config.vm.provision :ansible do |ansible|
    	ansible.playbook = "ansible.yml"
  end

end
