
from datetime import datetime
import json
from database import MysqlConnection

# Função para formatar as datas em cada item do JSON
# def formatar_datas(item):
    # item['created_at'] = datetime.strptime(item['created_at'], "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d %H:%M:%S")
    # item['updated_at'] = datetime.strptime(item['updated_at'], "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d %H:%M:%S")


# Aplicar a função a cada item na lista
def validar(data,data_embarcado):
    global create_web,atualizado_web
    data = data
    data_embarcado = data_embarcado
    # print(data)
    # for item in data:
    #     formatar_datas(item)

    # json_formatado = json.dumps(data, indent=4)
    # jsons = json.loads(json_formatado)
    criado_embarcado = data_embarcado[0]['dados_receita']['criado_em']
    # atualizado_embarcado = data_embarcado[0]['dados_receita']['atualizado_em']               
    create_web = data[0]['criado_em']
    atualizado_web = data[0]['atualizado_em']
    print(f'embarcado:{criado_embarcado}')
    # print(f"hora:embarcado:{atualizado_embarcado}")
    print(f"hora criado web:{create_web}")
    print(f"hora atualizado web:{atualizado_web}")
    if criado_embarcado < atualizado_web:
        atualizar_dias_habilita(data)
        print("WEB MAIS ATUAL")
        return True
    elif criado_embarcado > atualizado_web:
        return False
    else:
        return "integrações atualizadas"


def atualizar_dias_habilita(jsons):
    dias_semana_habilita = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']

    # Assuming create_web is a list of items, and you want to check the presence of days in each item
    for item in jsons:
        # Check if 'dias_semana' key exists in the item dictionary
        if 'dias_semana' in item:
            # Assuming item['dias_semana'] is a string containing days of the week
            condicoes_dias_semana = {dia: 1 if dia in item['dias_semana'] else 0 for dia in dias_semana_habilita}
            print(condicoes_dias_semana)
            dom = condicoes_dias_semana['Domingo']
            seg = condicoes_dias_semana['Segunda']
            ter = condicoes_dias_semana['Terça']
            quar = condicoes_dias_semana['Quarta']
            quin = condicoes_dias_semana['Quinta']
            sex = condicoes_dias_semana['Sexta']
            sab = condicoes_dias_semana['Sábado']
            db = MysqlConnection()


        valores = []


        if 'temperatura_minima' in item and item['temperatura_minima'] is not None:
            temp_min = float(jsons[0]['temperatura_minima'])
            intervaloTemp_habilita = 1
        else:
            temp_min = None
            intervaloTemp_habilita = 0

        if 'temperatura_maxima' in item and item['temperatura_maxima'] is not None:
            temp_max = float(jsons[0]['temperatura_maxima'])
            intervaloTemp_habilita = 1
        else:
            temp_max = None
            intervaloTemp_habilita = 0



        if 'hora_inicial' in item and item['hora_inicial'] is not None:
            hora_inicial_str = jsons[0]['hora_inicial']
            hora_inicial = int(datetime.strptime(hora_inicial_str, "%H:%M:%S").strftime("%H"))
            intervaloHorario_habilita = 1
        else:
            hora_inicial = None
            intervaloHorario_habilita = 0


        if 'hora_inicial' in item and item['hora_inicial'] is not None:
            min_inicial_str = jsons[0]['hora_inicial']
            min_inicial = int(datetime.strptime(min_inicial_str, "%H:%M:%S").strftime("%M"))
            intervaloHorario_habilita = 1

        else:
            min_inicial = None
            intervaloHorario_habilita = 0



        if 'hora_final' in item and item['hora_final'] is not None:
            hora_final_str = jsons[0]['hora_final']
            hora_final = int(datetime.strptime(hora_final_str, "%H:%M:%S").strftime("%H"))
            intervaloHorario_habilita = 1
        else:
            hora_final = None
            intervaloHorario_habilita = 0



        if 'hora_final' in item and item['hora_final'] is not None:
            hora_final_str = jsons[0]['hora_final']
            min_final = int(datetime.strptime(hora_final_str, "%H:%M:%S").strftime("%M"))
            intervaloHorario_habilita = 1
        else:
            min_final = 0
            intervaloHorario_habilita = 0##########



        if 'considerar_chuva' in item and item['considerar_chuva'] is not None:
            considerar_chuva = jsons[0]['considerar_chuva']
            chuva_habilita = 1
        else:
            considerar_chuva = None
            chuva_habilita = 0###########333333



        if 'umidade_minima' in item and item['umidade_minima'] is not None:
            umidade_minima = float(jsons[0]['umidade_minima'])
            umidade_habilita = 1
        else:
            umidade_minima = None
            umidade_habilita = 0#############



        if 'umidade_maxima' in item and item['umidade_maxima'] is not None:
                umidade_maxima = jsons[0]['umidade_maxima']
                umidade_habilita = 1
        else:
            umidade_maxima = None
            umidade_habilita = 0

        if 'ponto_orvalho' in item and item['ponto_orvalho'] is not None:
            ponto_orvalho = jsons[0]['ponto_orvalho']
            pontoOrvalho_habilita = 0
        else:
            ponto_orvalho = None
            pontoOrvalho_habilita = 0####
        

   
        


    db.set_query_receita_web(atualizado_web,
                             intervaloTemp_habilita,
                             intervaloHorario_habilita,
                             chuva_habilita,
                             umidade_habilita,
                             pontoOrvalho_habilita,
                             temp_min,
                             temp_max,
                             hora_inicial,
                             min_inicial,
                             hora_final,
                             min_final,
                             dom,
                             seg,
                             ter,
                             quar,
                             quin,
                             sex,
                             sab,
                             considerar_chuva,
                             umidade_minima,
                             umidade_maxima,
                             ponto_orvalho)

