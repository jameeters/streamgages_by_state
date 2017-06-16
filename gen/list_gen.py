from stream_gages.site_listing import get_sites

def make_list(state = 'MO'):
    with open ('../site/content/list_page.tile', 'w+') as output:
        raw = get_sites(state)
        headers = ['station_nm', 'site_no', 'huc_cd']
        _write_table_header(output, headers)

        for entry in raw:
            to_write = []
            for key in headers:
                try:
                    to_write.append(entry[key])
                except KeyError:
                    to_write.append('<KeyError>')
            _write_table_row(output, to_write)

    return


# raw should be a list of entries to be in the row
def _write_table_row (file, raw):
    for entry in raw:
        entry = entry.strip()
    row = '|'
    for entry in raw:
        row = row + entry + '|'
    file.write(row + '\n')
    return

def _write_table_header (file, raw):
    for entry in raw:
        entry = entry.strip()
    row = ''
    for entry in raw:
        row = row + '|_. ' + entry
    row = row + '|'
    file.write(row + '\n')
    return



