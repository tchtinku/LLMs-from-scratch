import subprocess


def test_gpt_class_finetune():
    command = ["python", "ch07/01_main-chapter-code/gpt_instruction_finetuning.py", "--test_mode"]

    result = subprocess.run(command, capture_output=True, text=True)
    assert result.returncode == 0, f"Script exited with errors: {result.stderr}"