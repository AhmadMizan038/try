saldo_awal = 5000
deposit = input('masukkan nominal yang ingin anda depositkan :')
saldo_akir = saldo_awal + int(deposit)
hutang = 50_000

if saldo_akir < hutang:
    print('saldo anda kurang')
else:
    print('hutang anda berhasil di bayar')

    
#user bisa bayar hutang jika saldo dia cukup atau lebih untuk membayar
#user tidak bisa bayar jika saldonya kurangg
#uigifuyf8y