out = gameoflife
sources = gameoflife.cpp
objects = $(sources:.cpp=.o)

$(out) : $(objects)
	$(CXX) $(objects) -o $(out)

%.d: %.cpp
	@set -e; rm -f $@; \
		$(CXX) -MM $(CPPFLAGS) $< > $@.$$$$; \
		sed 's,\($*\)\.o[ :]*,\1.o $@ : ,g' < $@.$$$$ > $@; \
		rm -f $@.$$$$

include $(sources:.cpp=.d)

.PHONY : clean run
clean:
	-rm $(sources:.cpp=.o) $(sources:.cpp=.d) $(out)
run:
	./$(out)
