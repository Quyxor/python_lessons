# Исключения

try:
    n = int(input())
    import fuck
except (ValueError, ImportError) as e:
    print(e)
# except ImportError as a:
#     print(a)
finally:
    print('Mne poh..')
