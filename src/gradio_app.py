import gradio as gr
import pandas as pd

from vacancy_searcher import VacancySearcher

vacancy_searcher = VacancySearcher()


def find_jobs(desired_position, experience_years, work_description, key_skills):
    resume_query = ".".join(
        [
            f"Желаемая позиция: {desired_position}",
            f"Лет опыта: {experience_years}",
            f"Ключевые навыки: {key_skills}" f"Опыт работы: {work_description}",
        ]
    )

    results = vacancy_searcher.search(resume_query, top_k=5)

    jobs_df = pd.DataFrame(results)
    return jobs_df


with gr.Blocks() as demo:
    gr.Markdown("# Поиск вакансий")
    gr.Markdown(
        "Введите желаемую должность, опыт работы и описание своего опыта работы, чтобы найти подходящие вакансии."
    )
    with gr.Row():
        desired_position = gr.Textbox(label="Желаемая должность")
        experience_years = gr.Textbox(label="Сколько лет опыта")
        key_skills = gr.Textbox(label="Ключевые навыки")
    with gr.Row():
        work_description = gr.Textbox(lines=4, label="Описание опыта работы")
    with gr.Row():
        submit_button = gr.Button("Подобрать вакансии")
    output = gr.Dataframe(interactive=True)

    submit_button.click(
        find_jobs,
        inputs=[desired_position, experience_years, work_description, key_skills],
        outputs=output,
    )

demo.launch()
