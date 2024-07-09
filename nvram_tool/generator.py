class ConfGenerator:
    @staticmethod
    def generate_conf_h(blocks, output_path):
        with open(output_path, 'w') as file:
            file.write("#ifndef _CONF_H\n")
            file.write("#define _CONF_H\n")
            file.write("#include \"nvmaems_msg.h\" \n")
            file.write("#include \"aemsrnm_nvm_writeonfly.h\" \n\n\n\n")
            #print(f"\n Les differents Blocs à traiter sont les suivants:\n")  # Debugging line
            for block in blocks:
                with open('../output/statusBlockLogs.txt', 'a') as log_file:
                    log_file.write(f"\nTraitement du bloc [{block.name}].....:\n")
                    print(f"\nTraitement du bloc [{block.name}].....:\n")  # Debugging line
                    is_valid, error_message = block.is_valid()
                    if is_valid:
                        log_file.write(f"le Bloc {block.name} est [Valide] car il respecte toutes les conditions \n\n")
                        print(f"le Bloc {block.name} est [Valide] car il respecte toutes les conditions \n\n")  # Debugging line
                        file.write(block.to_c_struct())
                    else:
                        log_file.write(f"Le Bloc {block.name} est  [Invalide] Car: {error_message}\n")
                        print(f"Le Bloc {block.name} est  [Invalide] Car: {error_message}\n")  # Debugging line
            file.write("#endif // CONF_H\n")
