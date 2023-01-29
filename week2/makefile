residual/build: residual.cpp
	@echo "compiling..."
	c++ -framework Accelerate -o residual residual.cpp
residual/run: 
	./residual
residual/clean:
	rm residual

kahan/build: harmonic_kahan.cpp
	@echo "compiling..."
	c++ -o harmonic_kahan harmonic_kahan.cpp
kahan/run: 
	./harmonic_kahan
kahan/clean:
	rm harmonic_kahan