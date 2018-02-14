class analyze_input_data:
    filename = 'database.txt'

    def read_data_base(self):
        pos = []
        Efield = []
        with open(filename,'r') as file_to_read:
            while True:
                lines = file_to_read.readline()
                if not lines:
                    break
                    pass
                 p_tmp,E_tmp = [float(i) for i in lines.split()]
                 pos.append(p_tmp)
                 Efield.append(E_tmp)
                 pass
                pos = np.array(pos)
                Efield = np.array(Efield)
                pass
