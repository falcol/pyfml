defmodule Ex76 do
  @doc """
  Tạo một mật khẩu ngẫu nhiên (random password),
  mật khẩu này bắt buộc phải chứa ít nhất 1 chữ thường,
  1 chữ hoa, 1 số, 1 ký tự punctuation (string.punctuation).
  """
  def solve(length) do
    generate_password(length)
  end

  def generate_password(length \\ 16) do
    # generated by
    # $ python -c 'import string; print([ord(i) for i in string.punctuation])
    # then hand convert to Elixir range
    puncs =
      Enum.to_list(33..47) ++ Enum.to_list(58..64) ++ Enum.to_list(91..96) ++ [123, 124, 125, 126]

    number = Enum.take_random(0..9, 1) |> List.first() |> Integer.to_charlist()
    lower = Enum.take_random(?a..?z, 1)
    upper = Enum.take_random(?A..?Z, 1)

    all_chars = Enum.to_list(?a..?z) ++ Enum.to_list(?A..?Z) ++ puncs ++ Enum.to_list(0..9)

    List.to_string(
      lower ++
        upper ++ Enum.take_random(puncs, 1) ++ number ++ Enum.take_random(all_chars, length - 4)
    )
  end
end