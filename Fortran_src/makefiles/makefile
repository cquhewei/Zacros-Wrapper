COMPILER = gfortran

OUTPUT := ./zacros.x

FLAGS := -O2 -ffree-line-length-1024
LIBS := 

SOURCE = compat constants_module parser_module heap_functions_module graph_functions_module gauss_quadrature_module mt19937_module random_deviates_module error_module lattice_setup_module simulation_setup_module energetics_setup_module mechanism_setup_module state_setup_module lattice_handle_module energetics_handle_module rates_handle_module kmc_simulation_handle_module sampling_handle_module output_handle_module restarts_module 

EXECUTABLE = zacros_main

OBJS = $(SOURCE:%=%.o)
ALL_OBJS = $(SOURCE:%=%.o) $(EXECUTABLE:%=%.o)

.PHONY : all
all: $(ALL_OBJS) $(EXECUTABLE)

.PHONY : clean
clean:
	@echo "Cleaning directory"
	@\rm -rf *.o *.mod *.exe $(OUTPUT) 

%.o: ../%.f90
	@echo "Compiling: " $*
	$(COMPILER) -c  ${FLAGS} $< -o $@	

%:  %.o $(ALL_OBJS) 
	@echo "    Linking program:   " $@ 	
	$(COMPILER) $(FLAGS) $(ALL_OBJS) $(LIBS) -o $(OUTPUT)

