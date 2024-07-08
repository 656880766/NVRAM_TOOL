class ConfGenerator:
    @staticmethod
    def generate_conf_h(blocks, output_path):
        with open(output_path, 'w') as file:
            file.write("#ifndef CONF_H\n")
            file.write("#define CONF_H\n\n")
            for block in blocks:
                print(f"Traitement du bloc: {block}")  # Debugging line
                if block.is_valid():
                    print(f"Bloc Valide: {block.name}")  # Debugging line
                    file.write(block.to_c_struct())
                else:
                    print(f"Block Invalide: {block.name}")  # Debugging line
            file.write("#endif // CONF_H\n")
