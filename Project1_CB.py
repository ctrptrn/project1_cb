# Variable
menu = ['1. Laporan PO',
        '2. Membuat PO Baru',
        '3. Mengubah Data PO',
        '4. Menghapus Data PO',
        '5. Exit']

items = [{'nomor_po': 'A001', 'category': 'Wet Food', 'item_name': 'Whiskas', 'harga': '10000', 'jumlah_item': '20'},
{'nomor_po': 'A002', 'category': 'Dry Food', 'item_name': 'Royal Canin', 'harga': '50000', 'jumlah_item': '10'}]


# Main Menu
def menu():
    option = True
    while option != '5':
        print('---------------------------------------------------')
        print('\n==========Record PO Warung Pompom==========\n')
        print('1. Laporan PO')
        print('2. Membuat PO Baru')
        print('3. Mengubah Data PO')
        print('4. Menghapus Data PO')
        print('5. Exit\n')
        print('----------------------------------------------------')
        option = input('Pilih menu Record PO [1-5]:')
        if option == '1':
            read_data()
        elif option == '2':
            create_data()
        elif option == '3':
            edit_data()
        elif option == '4':
            delete_data()
        elif option == '5':
            print('********************')
            print('\nGood Bye\n')
            print('********************')


# Report Data Function
def read_data():
    read = True
    while read != '3':
        print('----------------------------------------------------')
        print('\n+++++++Laporan PO+++++++\n')
        print('1. Tampilkan semua laporan')
        print('2. Tampilkan laporan tertentu')
        print('3. Kembali ke Menu Utama\n')
        print('----------------------------------------------------')
        read = input('Pilih sub menu Laporan PO [1-3]:')
        if read == '1':
            if len(items) != 0:
                print('List PO :')
                for idx, product in enumerate(items):
                    print(f"{idx+1}. Nomor PO : {product['nomor_po']}, Category : {product['category']}, Item Name : {product['item_name']}, Harga : {product['harga']}, Total Item Penjualan : {product['jumlah_item']}")
            else:
                print('**********************')
                print('\nTidak ada PO\n')
                print('**********************')
            continue
        elif read == '2':
            if len(items) != 0:
                item = input('Masukkan Nomor PO :').upper()
                print(f"Data PO : {item}")
                found = False
                for idx, product in enumerate(items):
                    if product['nomor_po'] == item:
                        print(f"{idx+1}. Nomor PO : {product['nomor_po']}, Category : {product['category']}, Item Name : {product['item_name']}, Harga : {product['harga']}, Total Item Penjualan : {product['jumlah_item']}")
                        found = True
                        break
                if not found:
                    print('***********************')
                    print('\nNomor PO Tidak Ditemukan\n')
                    print('***********************')
        elif read == '3':
            break
        else:
            print('***********************')
            print('\nPilihan Menu Tidak Ada\n')
            print('***********************')
    return


# Tambah Pesanan Function
def create_data():
    create = True
    while create not in ['1', '2']:
        print('----------------------------------------------------')
        print('\n++++++++Membuat PO Baru++++++++\n')
        print('1. Buat PO Baru')
        print('2. Kembali ke Menu Utama\n')
        print('----------------------------------------------------')
        create = input('Pilih sub menu Buat PO Baru [1-2]:')
        if create == '2':
            menu()
        elif create == '1':
            nomor_po = input('Masukkan Nomor PO :')
            duplicate = False
            for product in items:
                if product['nomor_po'].lower() == nomor_po.lower():
                    duplicate = True
            if duplicate:
                print('********************')
                print('\nPO Sudah Ada\n')
                print('********************')
                create_data()
            else:
                print('-----------')
                print('Create PO :')
                print('-----------')
                item_name = input('Masukkan item name :')
                category = input('Masukkan category :')
                harga = input('Masukkan harga :')
                jumlah_item = input('Masukkan total item :')
                new_item = {
                    'nomor_po': nomor_po,
                    'item_name': item_name,
                    'category': category,
                    'harga': harga,
                    'jumlah_item': jumlah_item}
                confirm = 'True'
                while confirm.lower() not in ['y', 'n']:
                    confirm = input('Apakah PO akan disimpan (Y/N?):')
                    if confirm.lower() == 'y':
                        items.append(new_item)
                        print('********************')
                        print('\nPO berhasil disimpan\n')
                        print('********************')
                    elif confirm.lower() =='n':
                        print('********************')
                        print('\nPO tidak disimpan\n')
                        print('********************')
                        create_data()


# Edit Pesanan Function
def edit_data():
    edit = True
    while edit != '2':
        print('----------------------------------------------------')
        print('\n================Mengubah Data PO================\n')
        print('1. Ubah PO')
        print('2. Kembali ke Menu Utama\n')
        print('----------------------------------------------------')
        edit = input('Pilih sub menu Mengubah PO [1-2]:')
        if edit == '2':
            menu()
        elif edit == '1':
            nomor_po = input('Masukkan Nomor PO :')
            found = -1
            for idx, product in enumerate(items):
                if product['nomor_po'].lower() == nomor_po.lower():
                    found = idx
            if found != -1:
                confirm = 'True'
                while confirm.lower() not in ['y', 'n']:
                    print(f"Nomor PO : {items[found]['nomor_po']}, Category : {items[found]['category']}, Item Name : {items[found]['item_name']}, Harga : {items[found]['harga']}, Total Item Penjualan : {items[found]['jumlah_item']}")
                    confirm = input('Tekan Y jika ingin lanjut ubah PO atau N jika ingin membatalkan (Y/N):')
                    if confirm.lower() == 'y':
                        edit_po = input('Masukkan kolom PO yang ingin ubah :')
                        if edit_po.lower() == 'name':
                            new_name = input('Masukkan item name baru :')
                            items[found]['item_name'] = new_name
                            confirm2 = 'True'
                            while confirm2.lower() not in ['y', 'n']:
                                confirm2 = input('Apakah data ingin di ubah? (Y/N) :')
                                if confirm2.lower() == 'y':
                                    items[found]['item_name'] = new_name
                                    print('*********************')
                                    print('\nData Berhasil di ubah\n')
                                    print('*********************')
                                elif confirm2.lower() == 'n':
                                    print('*********************')
                                    print('\nData Tidak di ubah\n')
                                    print('*********************')
                        elif edit_po.lower() == 'jumlah item':
                            new_jumlah_item = input('Masukkan jumlah total item penjualan baru :')
                            items[found]['jumlah_item'] = new_jumlah_item
                            confirm2 = 'True'
                            while confirm2.lower() not in ['y', 'n']:
                                confirm2 = input('Apakah data ingin di ubah? (Y/N) :')
                                if confirm2.lower() == 'y':
                                    items[found]['jumlah_item'] = new_jumlah_item
                                    print('*********************')
                                    print('\nData Berhasil di ubah\n')
                                    print('*********************')
                                elif confirm2.lower() == 'n':
                                    print('*********************')
                                    print('\nData Tidak di ubah\n')
                                    print('*********************')
                        elif edit_po.lower() == 'category':
                            new_category = input('Masukkan kategori baru :')
                            items[found]['category'] = new_category
                            confirm2 = 'True'
                            while confirm2.lower() not in ['y', 'n']:
                                confirm2 = input('Apakah data ingin di ubah? (Y/N) :')
                                if confirm2.lower() == 'y':
                                    items[found]['category'] = new_category
                                    print('*********************')
                                    print('\nData Berhasil di ubah\n')
                                    print('*********************')
                                elif confirm2.lower() == 'n':
                                    print('*********************')
                                    print('\nData Tidak di ubah\n')
                                    print('*********************')
                        elif edit_po.lower() == 'harga':
                            new_harga = input('Masukkan harga baru :')
                            confirm2 = 'True'
                            while confirm2.lower() not in ['y', 'n']:
                                confirm2 = input('Apakah data ingin di ubah? (Y/N) :')
                                if confirm2.lower() == 'y':
                                    items[found]['harga'] = new_harga
                                    print('*********************')
                                    print('\nData Berhasil di ubah\n')
                                    print('*********************')
                                elif confirm2.lower() == 'n':
                                    print('*********************')
                                    print('\nData Tidak di ubah\n')
                                    print('*********************')
                    elif confirm.lower() == 'n':
                        edit_data()
            else:
                print('*********************')
                print('\nTidak Ada PO\n')
                print('*********************')
                edit_data()


# Hapus Data Function
def delete_data():
    delete = True
    while delete != '2':
        print('----------------------------------------------------')
        print('\n================Menghapus Data PO================\n')
        print('1. Hapus PO')
        print('2. Kembali ke Menu Utama\n')
        print('----------------------------------------------------')
        delete = input('Pilih sub menu Hapus Data PO[1-2]:')
        if delete == '2':
            menu()
        elif delete == '1':
            nomor_po = input('Masukkan Nomor PO :')
            found = -1
            for idx, product in enumerate(items):
                if product['nomor_po'] == nomor_po:
                    found = idx
            if found != -1:
                confirm = 'True'
                while confirm.lower() not in ['y', 'n']:
                    confirm = input('Apakah PO akan dihapus? (Y/N):')
                    if confirm.lower() == 'y':
                        print('*********************')
                        print('\nPO Terhapus\n')
                        print('*********************')
                        items.pop(found)
                    elif confirm.lower() == 'n':
                        delete_data()
            else:
                print('*********************')
                print('\nTidak Ada PO\n')
                print('*********************')
                delete_data()
menu()
