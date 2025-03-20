import gspread
import pandas as pd
from google.oauth2.service_account import Credentials
import inspect

def atualizar_gsheet(spreadsheet_url, spreadsheet_aba, excel_file):
    print("🟡 " + inspect.currentframe().f_code.co_name)
    # 1. Defina o caminho para o arquivo de credenciais
    SERVICE_ACCOUNT_FILE = "api_google_sheets.json"

    # 2. Defina o escopo de permissões
    SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]

    # 3. Autentique usando as credenciais do Service Account
    credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    client = gspread.authorize(credentials)

    # 4. Abra a planilha do Google pelo URL
    spreadsheet = client.open_by_url(spreadsheet_url)

    # 5. Selecione a aba que deseja atualizar
    worksheet = spreadsheet.worksheet(spreadsheet_aba)

    # 6. Leia o arquivo Excel com pandas
    df = pd.read_excel(excel_file)
    df = df.astype(str)
    df = df.fillna('')

    # 7. Limpe a aba atual para substituir todos os dados
    worksheet.clear()

    # 8. Atualize com os novos dados do DataFrame
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())
    print("🟢 " + inspect.currentframe().f_code.co_name)

    
