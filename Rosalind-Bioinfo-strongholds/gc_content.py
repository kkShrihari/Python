def GC_content(data):
        '''
        adds up the (no of g and c in sequence)*100 and divided by total no of nucleotides 
        GC(%) = (total.g + total.c)*100/total.nucleotides
        '''
        # Loops through the sequence
        
        data = data.strip().split('>')
        data =  [i for i in data if i != ""]
        
        result_dict = {}
        for lst in data:
            lst = lst.splitlines()
            k = lst[0]
            val = str("".join(map(str,lst[1:])))
            result_dict[k] = val
        

        final_dict = {}
        for i in result_dict:
            g,c = 0,0
            for i0 in result_dict[i]:
                if i0 == "G":
                    g += 1
                if i0 == "C":
                    c += 1
            seq_length = len(result_dict[i])
            GC_percent = (g + c)*100/seq_length
            final_dict[i] = (GC_percent)
        max_key = max(final_dict, key=final_dict.get)
        result = max_key + "\n" + str(final_dict[max_key])
        return result


