import pytest

lam=lambda x,y:x+y
a = ['sdf','h']

class Test_demo:
  @pytest.mark.fff
  def test_1(self):
    print('hohoho')
    assert 'h'in a

  def test_2(self):
    print('hahahah')
    assert lam(2, 3) == 6

if __name__ == '__main__':
   args = ['-s','-q','-m', 'fff']
   pytest.main(args)