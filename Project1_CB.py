# Variable
menu = ['1. Laporan Stock Item',
        '2. Tambah Stock Item',
        '3. Mengubah Stock Item',
        '4. Hapus Stock Item',
        '5. Exit']

items = [{'item_code': 'A001', 'category': 'Wet Food', 'item_name': 'Whiskas', 'harga': '10000', 'stock': '20'},
{'item_code': 'A002', 'category': 'Dry Food', 'item_name': 'Royal Canin', 'harga': '50000', 'stock': '10'}]


# Main Menu
def menu():
    option = True
    while option != '5':
        print('---------------------------------------------------')
        print('\n==========Record Stock Item Warung Pompom==========\n')
        print('1. Laporan Stock Item')
        print('2. Tambah Stock Item')
        print('3. Edit Stock Item')
        print('4. Hapus Stock Item')
        print('5. Exit\n')
        print('----------------------------------------------------')
        option = input('Pilih sub menu Record Stock Item [1-5]:')
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
            print('\nPilihan menu salah\n')
            print('********************')


# Report Data Function
def read_data():
    read = True
    while read != '3':
        print('----------------------------------------------------')
        print('\n+++++++Laporan Stock Item+++++++\n')
        print('1. Tampilkan semua laporan')
        print('2. Tampilkan laporan tertentu')
        print('3. Kembali ke Menu Utama\n')
        print('----------------------------------------------------')
        read = input('Pilih sub menu Laporan Stock Item [1-3]:')
        if read == '1':
            if len(items) != 0:
                print('List Stock Item :')
                for idx, product in enumerate(items):
                    print(f"{idx+1}. Item Code : {product['item_code']}, Category : {product['category']}, Item Name : {product['item_name']}, Harga : {product['harga']}, Stock : {product['stock']}")
            else:
                print('**********************')
                print('\nTidak ada Data Item\n')
                print('**********************')
            continue
        elif read == '2':
            if len(items) != 0:
                item = input('Input Item Code :').upper()
                print(f"Data Item code : {item}")
                found = False
                for idx, product in enumerate(items):
                    if product['item_code'] == item:
                        print(f"{idx+1}. Item Code : {product['item_code']}, Category : {product['category']}, Item Name : {product['item_name']}, Harga : {product['harga']}, Stock : {product['stock']}")
                        found = True
                        break
                if not found:
                    print('***********************')
                    print('\nItem Tidak Terdaftar\n')
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
        print('\n++++++++Tambah Stock Item++++++++\n')
        print('1. Tambah Stock Item')
        print('2. Kembali ke Menu Utama\n')
        print('----------------------------------------------------')
        create = input('Pilih sub menu Tambah Stock Item [1-2]:')
        if create == '2':
            menu()
        elif create == '1':
            item_code = input('Masukkan Item Code :')
            duplicate = False
            for product in items:
                if product['item_code'] == item_code:
                    duplicate = True
            if duplicate:
                print('********************')
                print('\nStock Item Sudah Ada\n')
                print('********************')
            else:
                print('Create Item :')
                item_name = input('Masukkan item name :')
                category = input('Masukkan category :')
                harga = input('Masukkan harga :')
                stock = input('Masukkan stock :')
                new_item = {
                    'item_code': item_code,
                    'category': category,
                    'item_name': item_name,
                    'harga': harga,
                    'stock': stock}
                confirm = 'True'
                while confirm.lower() not in ['y', 'n']:
                    confirm = input('Apakah Item akan disimpan (Y/N?):')
                    if confirm.lower() == 'y':
                        items.append(new_item)
                    else:
                        create_data()


# Edit Pesanan Function
def edit_data():
    edit = True
    while edit != '2':
        print('----------------------------------------------------')
        print('\n================Mengubah Stock Item================\n')
        print('1. Ubah Stock Item')
        print('2. Kembali ke Menu Utama\n')
        print('----------------------------------------------------')
        edit = input('Pilih sub menu Mengubah Stock Item [1-2]:')
        if edit == '2':
            menu()
        elif edit == '1':
            item_code = input('Masukkan Item Code :')
            found = -1
            for idx, product in enumerate(items):
                if product['item_code'].lower() == item_code:
                    found = idx
            if found != -1:
                confirm = 'True'
                while confirm.lower() not in ['y', 'n']:
                    print(f"Item Code : {items[found]['item_code']}, Category : {items[found]['category']}, Item Name : {items[found]['item_name']}, Harga : {items[found]['harga']}, Stock : {items[found]['stock']}")
                    confirm = input('Tekan Y jika ingin lanjut ubah Item atau N jika ingin membatalkan (Y/N):')
                    if confirm.lower() == 'y':
                        edit_item = input('Masukkan kolom yang ingin ubah :')
                        if edit_item.lower() == 'name':
                            new_name = input('Masukkan item name baru :')
                            items[found]['item_name'] = new_name
                            confirm2 = 'True'
                            while confirm2.lower() not in ['y', 'n']:
                                confirm2 = input('Apakah data ingin di ubah? (Y/N) :')
                                if confirm2.lower() == 'y':
                                    items[found]['harga'] = new_name
                                    print('*********************')
                                    print('\nData Berhasil di ubah\n')
                                    print('*********************')
                                elif confirm2.lower() == 'n':
                                    print('*********************')
                                    print('\nData Tidak di ubah\n')
                                    print('*********************')
                        elif edit_item.lower() == 'stock':
                            new_stock = input('Masukkan jumlah stock baru :')
                            items[found]['stock'] = new_stock
                            confirm2 = 'True'
                            while confirm2.lower() not in ['y', 'n']:
                                confirm2 = input('Apakah data ingin di ubah? (Y/N) :')
                                if confirm2.lower() == 'y':
                                    items[found]['harga'] = new_stock
                                    print('*********************')
                                    print('\nData Berhasil di ubah\n')
                                    print('*********************')
                                elif confirm2.lower() == 'n':
                                    print('*********************')
                                    print('\nData Tidak di ubah\n')
                                    print('*********************')
                        elif edit_item.lower() == 'category':
                            new_category = input('Masukkan kategori baru :')
                            items[found]['category'] = new_category
                            confirm2 = 'True'
                            while confirm2.lower() not in ['y', 'n']:
                                confirm2 = input('Apakah data ingin di ubah? (Y/N) :')
                                if confirm2.lower() == 'y':
                                    items[found]['harga'] = new_category
                                    print('*********************')
                                    print('\nData Berhasil di ubah\n')
                                    print('*********************')
                                elif confirm2.lower() == 'n':
                                    print('*********************')
                                    print('\nData Tidak di ubah\n')
                                    print('*********************')
                        elif edit_item.lower() == 'harga':
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
                print('\nTidak Ada Item\n')
                print('*********************')
                edit_data()


# Hapus Data Function
def delete_data():
    delete = True
    while delete != '2':
        print('----------------------------------------------------')
        print('\n================Menghapus Stock Item================\n')
        print('1. Hapus Stock Item')
        print('2. Kembali ke Menu Utama\n')
        print('----------------------------------------------------')
        delete = input('Pilih sub menu Hapus Stock Item [1-2]:')
        if delete == '2':
            menu()
        elif delete == '1':
            item_code = input('Masukkan Item Code :')
            found = -1
            for idx, product in enumerate(items):
                if product['item_code'] == item_code:
                    found = idx
            if found != -1:
                confirm = 'True'
                while confirm.lower() not in ['y', 'n']:
                    confirm = input('Apakah item akan dihapus? (Y/N):')
                    if confirm.lower() == 'y':
                        print('*********************')
                        print('\nItem Terhapus\n')
                        print('*********************')
                        items.pop(found)
                    elif confirm.lower() == 'n':
                        delete_data()
            else:
                print('*********************')
                print('\nTidak Ada Item\n')
                print('*********************')
                delete_data()
menu()