
architecture RTL of FIFO is begin end architecture;
architecture RTL of FIFO is begin end architecture;
architecture RTL of FIFO is begin end architecture;

-- This should fail
architecture RTL of FIFO is
  signal a : std_logic;
begin
  a <= b after 1 ns;
end architecture;

-- This should not fail
architecture RTL of FIFO is

  signal a : std_logic;

begin

  a <= b after 1 ns;

end architecture;
