import os
import pandas as pd

INPUT_FILE_PATH = 'Mes Anterior.xlsx'
OUTPUT_FILE_PATH = 'transacciones.xlsx'
MES_ANTERIOR = 'Mes 3'


def write_new_sheet(row, new_file=True):
    df_out = pd.DataFrame()
    df_out['Mes'] = [MES_ANTERIOR]
    df_out['# de trans'] = [row['# de transacciones']]

    if new_file:
        df_out.transpose().to_excel(
            OUTPUT_FILE_PATH,
            sheet_name=row['Cía'],
            header=False
        )
    else:
        with pd.ExcelWriter(OUTPUT_FILE_PATH, engine='openpyxl', mode='a') as writer:
            df_out.transpose().to_excel(
                writer,
                sheet_name=row['Cía'],
                header=False
            )


def main():
    df = pd.read_excel(INPUT_FILE_PATH)

    for _, row in df.iterrows():
        if os.path.exists(OUTPUT_FILE_PATH):
            try:
                df_out = pd.read_excel(OUTPUT_FILE_PATH,
                                       sheet_name=row['Cía']).transpose()
                df_out.reset_index(inplace=True)
                df_out.columns = df_out.iloc[0].values
                df_out = df_out[1:]
                if MES_ANTERIOR in df_out['Mes'].values:
                    df_out.loc[
                        df_out['Mes'] == MES_ANTERIOR, '# de trans'
                    ] = row['# de transacciones']
                else:
                    df_out = pd.concat([
                        df_out,
                        pd.DataFrame({
                            'Mes': [MES_ANTERIOR],
                            '# de trans': [row['# de transacciones']]
                        })
                    ])

                with pd.ExcelWriter(OUTPUT_FILE_PATH, engine='openpyxl',
                                    mode='a', if_sheet_exists='replace') as writer:
                    df_out.transpose().to_excel(
                        writer,
                        sheet_name=row['Cía'],
                        header=False
                    )

            except ValueError:
                write_new_sheet(row, new_file=False)

        else:
            write_new_sheet(row)


if __name__ == '__main__':
    main()
